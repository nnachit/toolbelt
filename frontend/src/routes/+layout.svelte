<script lang="ts">
	import '../app.css';
	import { Alert } from "flowbite-svelte";

	let { children } = $props();
</script>

{@render children()}

<!-- Wrapper color background #101828 and light gray text -->
<main class="space-y-6 bg-[#101828] text-gray-300">
  <div class="p-8">
    <Alert color="secondary">
      <span class="font-medium">Info alert!</span>
      Change a few things up and try submitting again.
    </Alert>
  </div>
</main>
