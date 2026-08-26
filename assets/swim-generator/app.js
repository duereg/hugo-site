import _ from 'lodash';
import {
  generateWorkout,
  generateCssWorkout,
  listPresetPlans,
  generatePresetPlan,
} from 'swim-generator/lib/index.js';
import './app.css';

const templateString =
  '<li><%- number %>x<%- length %> <%- type %> @ <%- formatTime(time) %></li>';
const compiledTemplate = _.template(templateString);

function formatTime(secNum) {
  const minutes = Math.floor(secNum / 60);
  const seconds = secNum - minutes * 60;

  return _([minutes, seconds])
    .map((timeUnit) => (timeUnit < 10 ? '0' + timeUnit : timeUnit))
    .join(':');
}

function renderTextWorkout(workoutDiv, text) {
  const pre = document.createElement('pre');
  pre.textContent = text;
  workoutDiv.appendChild(pre);
}

function init() {
  const workoutTypeSelect = document.getElementById('workoutTypeSelect');
  const timeInputContainer = document.querySelector('.swim-generator--time-input');
  const cssInputsContainer = document.getElementById('cssInputsContainer');
  const presetInputsContainer = document.getElementById('presetInputsContainer');
  const presetPlanSelect = document.getElementById('presetPlanSelect');
  const generateBtn = document.getElementById('swimGenerateBtn');

  function populatePresetPlans() {
    presetPlanSelect.innerHTML = '';
    listPresetPlans().forEach((plan) => {
      const option = document.createElement('option');
      option.value = plan.id;
      option.textContent = plan.name;
      presetPlanSelect.appendChild(option);
    });
  }

  function handleWorkoutTypeChange() {
    const mode = workoutTypeSelect.value;
    timeInputContainer.style.display = mode === 'MIXED_UNDERWATERS' ? '' : 'none';
    cssInputsContainer.style.display =
      mode !== 'MIXED_UNDERWATERS' && mode !== 'PRESET_PLAN' ? '' : 'none';
    presetInputsContainer.style.display = mode === 'PRESET_PLAN' ? '' : 'none';
    if (mode === 'PRESET_PLAN') {
      populatePresetPlans();
    }
  }

  workoutTypeSelect.addEventListener('change', handleWorkoutTypeChange);
  handleWorkoutTypeChange();

  generateBtn.addEventListener('click', () => {
    const selectedWorkoutType = workoutTypeSelect.value;
    const timeDiv = document.getElementById('time');
    const workoutDiv = document.getElementById('workout');
    workoutDiv.innerHTML = '';

    if (selectedWorkoutType === 'MIXED_UNDERWATERS') {
      const timeInSeconds = document.getElementById('timeInput').value * 60;
      const workout = generateWorkout(timeInSeconds);

      timeDiv.innerHTML = 'Total Time: ' + formatTime(workout.seconds);
      const workoutMarkup = _.map(workout.intervals, (interval) =>
        compiledTemplate({ ...interval, formatTime })
      ).join(' ');
      workoutDiv.innerHTML = workoutMarkup;
    } else if (selectedWorkoutType === 'PRESET_PLAN') {
      const cssTime = document.getElementById('presetCssInput').value;
      const planId = presetPlanSelect.value;
      const includeExtras = document.getElementById('presetIncludeExtras').checked;
      const result = generatePresetPlan(planId, cssTime, { includeExtras });

      renderTextWorkout(workoutDiv, result);
      timeDiv.innerHTML = '';
    } else {
      const distance = parseInt(document.getElementById('distanceInput').value, 10);
      const cssTime = document.getElementById('cssInput').value;
      const workoutTypeOptionText =
        workoutTypeSelect.options[workoutTypeSelect.selectedIndex].text;
      const workoutType = workoutTypeOptionText.split(' ')[0];
      const energySystem = selectedWorkoutType;

      renderTextWorkout(
        workoutDiv,
        generateCssWorkout(distance, energySystem, cssTime, workoutType)
      );
      timeDiv.innerHTML = '';
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
