import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';

export default defineConfig({
  // Tu dominio real (importante para el SEO y sitemap)
  site: 'https://franciscoaleuy.ca',
  
  // La base debe ser la raíz, porque ya no usas la URL larga de GitHub
  base: '/', 
  
  integrations: [mdx(), react()],
});