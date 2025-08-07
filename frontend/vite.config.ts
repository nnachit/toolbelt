import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  resolve: {
    alias: {
      crypto: 'crypto-browserify',
      stream: 'stream-browserify'
    }
  },
  optimizeDeps: {
    include: ['crypto-browserify']
  },
  plugins: [
    tailwindcss(),
    sveltekit()],
  server: {
	proxy: {
	  '/api': {
		target: 'http://localhost:8000',
		changeOrigin: true,
		rewrite: path => path.replace(/^\/api/, '')
	  }
	}
  }
});
