<script lang="ts">
  import '../app.css';
  let { children } = $props();
</script>

<div class="flex h-screen bg-gray-900 text-gray-100">
  <!-- Sidebar -->
  <aside class="w-64 bg-gray-800 p-6">
    <div class="flex items-center mb-12">
      <img src="/logo.svg" alt="Logo" class="h-8 w-8 mr-2" />
      <span class="text-xl font-semibold">ToolBelt</span>
    </div>
    <nav class="space-y-4">
      <a href="/" class="flex items-center p-2 rounded-lg hover:bg-gray-700">
        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M3 12l2-2 7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2v10a1 1 0 01-1 1h-3m-6 0h6"/></svg>
        <span class="ml-3">Home</span>
      </a>
      <a href="/password" class="flex items-center p-2 rounded-lg hover:bg-gray-700">
        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 11c.706 0 1.402.105 2 .305M18 13v1a4 4 0 01-8 0v-1m-2 0v1a6 6 0 0012 0v-1m-6 4v2m0-4v-2m0-4V7m0 2h.01"/></svg>
        <span class="ml-3">Password</span>
      </a>
    </nav>
  </aside>

  <!-- Main content -->
  <div class="flex-1 flex flex-col">
    <main class="flex-1 overflow-auto p-6">
      {@render children()}
    </main>
  </div>
</div>