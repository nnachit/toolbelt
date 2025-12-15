<script lang="ts">
  import '../app.css';
  import { page } from '$app/stores';

  let { children } = $props();

  const navItems = [
    { href: '/', label: 'Home', icon: 'home' },
    { href: '/password', label: 'Password', icon: 'key' },
  ];
</script>

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
    <nav class="flex-1 px-4">
      <ul class="space-y-2">
        {#each navItems as item}
          {@const isActive = $page.url.pathname === item.href}
          <li>
            <a
              href={item.href}
              class="flex items-center gap-3 px-4 py-3 rounded-lg transition-colors {isActive ? 'bg-blue-600 text-white' : 'text-gray-400 hover:bg-gray-700 hover:text-white'}"
            >
              {#if item.icon === 'home'}
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
                </svg>
              {:else if item.icon === 'key'}
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path>
                </svg>
              {/if}
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
