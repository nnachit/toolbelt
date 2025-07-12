<script lang="ts">
	import '../app.css';
    import Logo from '../assets/images/svg-tmp.svg';
    import {goto} from "$app/navigation";

	let { children } = $props();
</script>

{@render children()}

<div class="flex flex-row">
  <div class="flex-1 flex flex-col items-center justify-center px-8 py-10 text-center gap-10">
    <div class="flex flex-col items-center justify-center w-full max-w-2xl gap-6 md:flex-row">
      <button
        id="application1"
        onclick={() => goto(`/application1`)}
        class="flex flex-col w-48 h-48 items-center p-6 transition-shadow duration-300 bg-white rounded-xl shadow-md hover:shadow-xl hover:scale-[1.02] ease-in-out"
      >
        <img src={Logo} alt="Application logo" class="h-16 mb-4" />
        <h2 class="text-2xl font-semibold text-blue-400">Application</h2>
      </button>
      <button
        id="application2"
        onclick={() => goto(`/application2`)}
        class="flex flex-col w-48 h-48 items-center p-6 transition-shadow duration-300 bg-white rounded-xl shadow-md hover:shadow-xl hover:scale-[1.02] ease-in-out"
      >
        <img src={Logo} alt="Application logo" class="h-16 mb-4" />
        <h2 class="text-2xl font-semibold text-blue-400">Application</h2>
      </button>
      <button
        id="application3"
        onclick={() => goto(`/application3`)}
        class="flex flex-col w-48 h-48 items-center p-6 transition-shadow duration-300 bg-white rounded-xl shadow-md hover:shadow-xl hover:scale-[1.02] ease-in-out"
      >
        <img src={Logo} alt="Application logo" class="h-16 mb-4" />
        <h2 class="text-2xl font-semibold text-blue-400">Application</h2>
      </button>
    </div>
  </div>
</div>
