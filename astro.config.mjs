import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';

export default defineConfig({
  site: 'https://franciscoaleuy.ca',
  base: '/', 
  
  // AGREGA ESTO: Renombramos la carpeta de salida para evitar el bloqueo de GitHub
  build: {
    assets: 'assets', 
  },

  integrations: [mdx(), react()],
});