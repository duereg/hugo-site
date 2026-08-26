import * as esbuild from 'esbuild';
import { mkdirSync } from 'fs';

mkdirSync('static/tourney', { recursive: true });

await esbuild.build({
  entryPoints: ['assets/tourney/main.tsx'],
  bundle: true,
  outfile: 'static/tourney/app.js',
  format: 'esm',
  platform: 'browser',
  target: ['es2020'],
  publicPath: '/tourney/',
  alias: {
    'tourney-time': 'tourney-time/dist/src/tourney-time.js',
  },
  loader: {
    '.tsx': 'tsx',
    '.ts': 'ts',
    '.css': 'css',
  },
  minify: true,
  sourcemap: true,
});

console.log('Built static/tourney/app.js');
