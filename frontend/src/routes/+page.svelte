<script lang="ts">
  import { tools } from '$lib/tools';
  import ToolIcon from '$lib/components/ToolIcon.svelte';
</script>

<div class="max-w-4xl mx-auto">
  <!-- Hero -->
  <div class="text-center mb-12">
    <h1 class="text-4xl font-bold mb-4">Welcome to ToolBelt</h1>
    <p class="text-gray-400 text-lg">A collection of developer utilities at your fingertips.</p>
  </div>

  <!-- Tools Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    {#each tools as tool}
      <a
        href={tool.available ? tool.href : '#'}
        class="block p-6 bg-gray-800 rounded-xl border border-gray-700 transition-all {tool.available ? 'hover:border-blue-500 hover:bg-gray-750 cursor-pointer' : 'opacity-50 cursor-not-allowed'}"
      >
        <div class="flex items-start gap-4">
          <div class="w-12 h-12 bg-gray-700 rounded-lg flex items-center justify-center flex-shrink-0 {tool.available ? 'text-blue-400' : 'text-gray-500'}">
            <ToolIcon name={tool.icon} class="w-6 h-6" />
          </div>
          <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
              <h2 class="text-lg font-semibold">{tool.title}</h2>
              {#if !tool.available}
                <span class="text-xs bg-gray-700 text-gray-400 px-2 py-0.5 rounded">Coming Soon</span>
              {/if}
            </div>
            <p class="text-gray-400 text-sm">{tool.description}</p>
          </div>
        </div>
      </a>
    {/each}
  </div>
</div>
