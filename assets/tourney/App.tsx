import React, { useState } from 'react';
import { TourneyForm, ResultsDisplay } from './components';
import tourneyTime, {
  TourneyTimeOptions,
  TourneyTimeResult,
} from 'tourney-time';

const App: React.FC = () => {
  const [results, setResults] = useState<TourneyTimeResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const defaultFormValues: Partial<TourneyTimeOptions> = {
    teams: 0,
    gameTime: 33,
    restTime: 7,
    areas: 1,
    playoffTime: 33,
    playoffRestTime: 12,
  };

  const handleCalculateSchedule = (
    options: Omit<TourneyTimeOptions, 'teams'> & { teams: number | string },
  ) => {
    try {
      setError(null);
      setResults(null);

      const numericTeams =
        typeof options.teams === 'string'
          ? parseInt(options.teams, 10)
          : options.teams;
      if (isNaN(numericTeams)) {
        throw new Error('Number of teams must be a valid number.');
      }

      const fullOptions: TourneyTimeOptions = {
        ...options,
        teams: numericTeams,
      };

      const calculatedResults = tourneyTime(fullOptions);
      setResults(calculatedResults);
    } catch (e: unknown) {
      const message =
        e instanceof Error ? e.message : 'An unknown error occurred.';
      setError(message);
      setResults(null);
    }
  };

  return (
    <div className="tourney-app">
      <TourneyForm
        onSubmit={handleCalculateSchedule}
        defaultValues={defaultFormValues}
      />
      <ResultsDisplay results={results} error={error} />
    </div>
  );
};

export default App;
