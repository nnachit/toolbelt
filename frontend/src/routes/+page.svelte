<script lang="ts">
  const tools = [
    {
      href: '/password',
      title: 'Password Generator',
      description: 'Generate secure, random passwords with customizable options.',
      icon: 'key',
      available: true
    },
    {
      href: '/base64',
      title: 'Base64 Encoder/Decoder',
      description: 'Encode and decode Base64 strings.',
      icon: 'code',
      available: true
    },
    {
      href: '/url-encoder',
      title: 'URL Encoder/Decoder',
      description: 'Encode and decode URL components.',
      icon: 'link',
      available: true
    },
    {
      href: '/html-entities',
      title: 'HTML Entity Encoder',
      description: 'Convert special characters to HTML entities.',
      icon: 'document',
      available: true
    },
    {
      href: '#',
      title: 'Hash Generator',
      description: 'Generate MD5, SHA-1, SHA-256 and other hash values.',
      icon: 'hash',
      available: false
    },
    {
      href: '#',
      title: 'UUID Generator',
      description: 'Generate random UUIDs (v4) or timestamp-based UUIDs (v1).',
      icon: 'fingerprint',
      available: false
    },
    {
      href: '#',
      title: 'JSON Formatter',
      description: 'Format, validate, and minify JSON.',
      icon: 'json',
      available: false
    },
    {
      href: '#',
      title: 'JWT Decoder',
      description: 'Decode and inspect JWT tokens.',
      icon: 'shield',
      available: false
    },
  ];
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
            {#if tool.icon === 'key'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path>
              </svg>
            {:else if tool.icon === 'hash'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14"></path>
              </svg>
            {:else if tool.icon === 'code'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
              </svg>
            {:else if tool.icon === 'fingerprint'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path>
              </svg>
            {:else if tool.icon === 'link'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path>
              </svg>
            {:else if tool.icon === 'document'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
              </svg>
            {:else if tool.icon === 'json'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2 1 3 3 3h10c2 0 3-1 3-3V7c0-2-1-3-3-3H7c-2 0-3 1-3 3zm4 3h8m-8 4h5"></path>
              </svg>
            {:else if tool.icon === 'shield'}
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
              </svg>
            {/if}
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
