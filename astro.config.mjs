import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

import react from '@astrojs/react';

export default defineConfig({
  site: 'https://fcoaleuy.github.io',
  base: '/personal-site/', 
  integrations: [mdx(), react()],
});