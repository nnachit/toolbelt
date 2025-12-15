<script lang="ts">
  import { onMount } from 'svelte';

  let password = $state('');
  let length = $state(16);
  let isLoading = $state(false);
  let copied = $state(false);
  let error = $state('');

  let includeLowercase = $state(true);
  let includeUppercase = $state(true);
  let includeNumbers = $state(true);
  let includeSpecial = $state(true);

  function calculateStrength(pwd: string): { score: number; label: string; color: string } {
    if (!pwd) return { score: 0, label: '', color: 'bg-gray-600' };

    let score = 0;

    // Length contribution
    if (pwd.length >= 8) score += 1;
    if (pwd.length >= 12) score += 1;
    if (pwd.length >= 16) score += 1;
    if (pwd.length >= 24) score += 1;

    // Character variety
    if (/[a-z]/.test(pwd)) score += 1;
    if (/[A-Z]/.test(pwd)) score += 1;
    if (/[0-9]/.test(pwd)) score += 1;
    if (/[^a-zA-Z0-9]/.test(pwd)) score += 1;

    if (score <= 2) return { score: 1, label: 'Weak', color: 'bg-red-500' };
    if (score <= 4) return { score: 2, label: 'Fair', color: 'bg-orange-500' };
    if (score <= 6) return { score: 3, label: 'Strong', color: 'bg-yellow-500' };
    return { score: 4, label: 'Very Strong', color: 'bg-green-500' };
  }

  let strength = $derived(calculateStrength(password));

  async function generatePassword() {
    if (!includeLowercase && !includeUppercase && !includeNumbers && !includeSpecial) {
      error = 'Select at least one character type';
      return;
    }

    error = '';
    isLoading = true;

    try {
      const params = new URLSearchParams({
        length: String(length),
        lower: includeLowercase ? 'true' : 'false',
        upper: includeUppercase ? 'true' : 'false',
        digits: includeNumbers ? 'true' : 'false',
        special: includeSpecial ? 'true' : 'false'
      });

      const res = await fetch(`/api/password/?${params.toString()}`);

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || `Error ${res.status}`);
      }

      const { password: pwd } = await res.json();
      password = pwd;
    } catch (err) {
      console.error(err);
      error = err instanceof Error ? err.message : 'Something went wrong';
    } finally {
      isLoading = false;
    }
  }

  async function copyToClipboard() {
    if (!password) return;

    try {
      await navigator.clipboard.writeText(password);
      copied = true;
      setTimeout(() => copied = false, 2000);
    } catch (err) {
      console.error('Failed to copy:', err);
    }
  }

  onMount(generatePassword);
</script>

<div class="max-w-lg mx-auto">
  <h1 class="text-3xl font-bold mb-8">Password Generator</h1>

  <!-- Password display -->
  <div class="mb-6">
    <div class="flex gap-2">
      <input
        class="flex-1 p-3 bg-gray-800 border border-gray-700 rounded-lg font-mono text-lg tracking-wider"
        readonly
        value={password}
        placeholder={isLoading ? 'Generating...' : 'Generated password'}
      />
      <button
        onclick={copyToClipboard}
        disabled={!password}
        class="px-4 py-2 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
        aria-label="Copy to clipboard"
      >
        {#if copied}
          <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
          </svg>
        {:else}
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
          </svg>
        {/if}
      </button>
      <button
        onclick={generatePassword}
        disabled={isLoading}
        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
        aria-label="Generate new password"
      >
        {#if isLoading}
          <svg class="w-6 h-6 animate-spin" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        {:else}
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
        {/if}
      </button>
    </div>

    <!-- Copied feedback -->
    {#if copied}
      <p class="text-green-400 text-sm mt-2">Copied to clipboard!</p>
    {/if}

    <!-- Error message -->
    {#if error}
      <p class="text-red-400 text-sm mt-2">{error}</p>
    {/if}
  </div>

  <!-- Strength indicator -->
  {#if password}
    <div class="mb-6">
      <div class="flex justify-between items-center mb-2">
        <span class="text-sm text-gray-400">Password Strength</span>
        <span class="text-sm font-medium">{strength.label}</span>
      </div>
      <div class="w-full h-2 bg-gray-700 rounded-full overflow-hidden">
        <div
          class="h-full transition-all duration-300 {strength.color}"
          style="width: {strength.score * 25}%"
        ></div>
      </div>
    </div>
  {/if}

  <!-- Length slider -->
  <div class="mb-6">
    <div class="flex justify-between items-center mb-2">
      <label for="password-length" class="text-sm text-gray-400">Length</label>
      <span class="text-sm font-medium bg-gray-800 px-2 py-1 rounded">{length}</span>
    </div>
    <input
      id="password-length"
      class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
      type="range"
      min="4"
      max="64"
      bind:value={length}
      oninput={generatePassword}
    />
    <div class="flex justify-between text-xs text-gray-500 mt-1">
      <span>4</span>
      <span>64</span>
    </div>
  </div>

  <!-- Character options -->
  <div class="space-y-3">
    <h2 class="text-sm text-gray-400 mb-3">Character Types</h2>

    <label class="flex items-center justify-between p-3 bg-gray-800 rounded-lg cursor-pointer hover:bg-gray-750">
      <div class="flex items-center gap-3">
        <span class="text-gray-400 font-mono text-sm">abc</span>
        <span>Lowercase</span>
      </div>
      <input
        type="checkbox"
        bind:checked={includeLowercase}
        onchange={generatePassword}
        class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-gray-900"
      />
    </label>

    <label class="flex items-center justify-between p-3 bg-gray-800 rounded-lg cursor-pointer hover:bg-gray-750">
      <div class="flex items-center gap-3">
        <span class="text-gray-400 font-mono text-sm">ABC</span>
        <span>Uppercase</span>
      </div>
      <input
        type="checkbox"
        bind:checked={includeUppercase}
        onchange={generatePassword}
        class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-gray-900"
      />
    </label>

    <label class="flex items-center justify-between p-3 bg-gray-800 rounded-lg cursor-pointer hover:bg-gray-750">
      <div class="flex items-center gap-3">
        <span class="text-gray-400 font-mono text-sm">123</span>
        <span>Numbers</span>
      </div>
      <input
        type="checkbox"
        bind:checked={includeNumbers}
        onchange={generatePassword}
        class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-gray-900"
      />
    </label>

    <label class="flex items-center justify-between p-3 bg-gray-800 rounded-lg cursor-pointer hover:bg-gray-750">
      <div class="flex items-center gap-3">
        <span class="text-gray-400 font-mono text-sm">!@#</span>
        <span>Special Characters</span>
      </div>
      <input
        type="checkbox"
        bind:checked={includeSpecial}
        onchange={generatePassword}
        class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-gray-900"
      />
    </label>
  </div>
</div>
