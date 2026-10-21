<script lang="ts">
  import '../app.css';
  import { page } from '$app/stores';
  import { tools, toolByPath } from '$lib/tools';
  import ToolIcon from '$lib/components/ToolIcon.svelte';

  let { children } = $props();

  const navItems = [
    { href: '/', label: 'Home', icon: 'home' as const },
    ...tools.filter((tool) => tool.available).map(({ href, label, icon }) => ({ href, label, icon }))
  ];

  const siteDescription = 'A collection of developer utilities at your fingertips.';

  let currentTool = $derived(toolByPath($page.url.pathname));
</script>

<svelte:head>
  <title>{currentTool ? `${currentTool.title} — ToolBelt` : 'ToolBelt'}</title>
  <meta name="description" content={currentTool?.description ?? siteDescription} />
</svelte:head>

<div class="flex h-screen bg-gray-900 text-gray-100">
  <!-- Sidebar -->
  <aside class="w-64 bg-gray-800 flex flex-col">
    <!-- Logo -->
    <div class="p-6">
      <a href="/" class="flex items-center gap-3">
        <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
        </div>
        <span class="text-xl font-bold">ToolBelt</span>
      </a>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 px-4 overflow-y-auto">
      <ul class="space-y-1">
        {#each navItems as item}
          {@const isActive = $page.url.pathname === item.href}
          <li>
            <a
              href={item.href}
              class="flex items-center gap-3 px-4 py-3 rounded-lg transition-colors {isActive ? 'bg-blue-600 text-white' : 'text-gray-400 hover:bg-gray-700 hover:text-white'}"
            >
              <ToolIcon name={item.icon} />
              <span>{item.label}</span>
            </a>
          </li>
        {/each}
      </ul>
    </nav>

    <!-- Footer -->
    <div class="p-4 border-t border-gray-700">
      <p class="text-xs text-gray-500 text-center">ToolBelt v0.1</p>
    </div>
  </aside>

  <!-- Main content -->
  <main class="flex-1 overflow-auto p-8">
    {@render children()}
  </main>
</div>
