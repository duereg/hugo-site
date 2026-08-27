import * as esbuild from 'esbuild';
import { mkdirSync } from 'fs';

mkdirSync('static/utilities/swim-generator', { recursive: true });

await esbuild.build({
  entryPoints: ['assets/swim-generator/app.js'],
  bundle: true,
  outfile: 'static/utilities/swim-generator/app.js',
  format: 'esm',
  platform: 'browser',
  target: ['es2020'],
  loader: {
    '.css': 'css',
  },
  minify: true,
  sourcemap: true,
});

console.log('Built static/utilities/swim-generator/app.js');
