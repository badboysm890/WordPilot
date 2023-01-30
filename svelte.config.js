import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	},

	preprocess: preprocess({
		scss: {
			prependData: '@import "src/styles/global.scss";'
		}
	})
};

export default config;
