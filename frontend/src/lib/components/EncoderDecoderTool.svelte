<script lang="ts">
  import type { Snippet } from 'svelte';

  type Mode = 'encode' | 'decode';

  interface Props {
    title: string;
    description: string;
    encodedLabel: string;
    decodePlaceholder?: string;
    encodeError?: string;
    decodeError?: string;
    transform: (input: string, mode: Mode) => string;
    controls?: Snippet<[Mode]>;
    info?: Snippet<[Mode]>;
    footer?: Snippet;
  }

  let {
    title,
    description,
    encodedLabel,
    decodePlaceholder = `Enter ${encodedLabel} to decode...`,
    encodeError = 'Encoding error',
    decodeError = 'Processing error',
    transform,
    controls,
    info,
    footer
  }: Props = $props();

  let input = $state('');
  let output = $state('');
  let mode = $state<Mode>('encode');
  let error = $state('');
  let copied = $state(false);

  function process() {
    error = '';
    if (!input) {
      output = '';
      return;
    }

    try {
      output = transform(input, mode);
    } catch (e) {
      error = mode === 'decode' ? decodeError : encodeError;
      output = '';
    }
  }

  function swap() {
    const temp = input;
    input = output;
    output = temp;
    mode = mode === 'encode' ? 'decode' : 'encode';
  }

  function clear() {
    input = '';
    output = '';
    error = '';
  }

  async function copyToClipboard() {
    if (!output) return;
    try {
      await navigator.clipboard.writeText(output);
      copied = true;
      setTimeout(() => copied = false, 2000);
    } catch (e) {
      console.error('Failed to copy:', e);
    }
  }

  $effect(() => {
    process();
  });
</script>

<div class="max-w-4xl mx-auto">
  <h1 class="text-3xl font-bold mb-2">{title}</h1>
  <p class="text-gray-400 mb-8">{description}</p>

  <!-- Mode Toggle -->
  <div class="flex flex-wrap gap-4 mb-6">
    <div class="flex gap-2">
      <button
        onclick={() => mode = 'encode'}
        class="px-4 py-2 rounded-lg transition-colors {mode === 'encode' ? 'bg-blue-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
      >
        Encode
      </button>
      <button
        onclick={() => mode = 'decode'}
        class="px-4 py-2 rounded-lg transition-colors {mode === 'decode' ? 'bg-blue-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
      >
        Decode
      </button>
    </div>
    {@render controls?.(mode)}
  </div>

  <!-- Info box -->
  {#if info}
    <div class="bg-gray-800 border border-gray-700 rounded-lg p-4 mb-6 text-sm">
      {@render info(mode)}
    </div>
  {/if}

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
    <!-- Input -->
    <div>
      <div class="flex justify-between items-center mb-2">
        <label for="input" class="text-sm text-gray-400">
          {mode === 'encode' ? 'Text' : encodedLabel}
        </label>
        <span class="text-xs text-gray-500">{input.length} chars</span>
      </div>
      <textarea
        id="input"
        bind:value={input}
        placeholder={mode === 'encode' ? 'Enter text to encode...' : decodePlaceholder}
        class="w-full h-64 p-4 bg-gray-800 border border-gray-700 rounded-lg font-mono text-sm resize-none focus:outline-none focus:border-blue-500"
      ></textarea>
    </div>

    <!-- Output -->
    <div>
      <div class="flex justify-between items-center mb-2">
        <label for="output" class="text-sm text-gray-400">
          {mode === 'encode' ? encodedLabel : 'Text'}
        </label>
        <span class="text-xs text-gray-500">{output.length} chars</span>
      </div>
      <textarea
        id="output"
        value={output}
        readonly
        placeholder="Result will appear here..."
        class="w-full h-64 p-4 bg-gray-800 border border-gray-700 rounded-lg font-mono text-sm resize-none focus:outline-none"
      ></textarea>
    </div>
  </div>

  <!-- Error -->
  {#if error}
    <p class="text-red-400 text-sm mt-4">{error}</p>
  {/if}

  <!-- Actions -->
  <div class="flex gap-3 mt-6">
    <button
      onclick={swap}
      disabled={!output}
      class="flex items-center gap-2 px-4 py-2 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"></path>
      </svg>
      Swap
    </button>
    <button
      onclick={copyToClipboard}
      disabled={!output}
      class="flex items-center gap-2 px-4 py-2 bg-gray-700 hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
    >
      {#if copied}
        <svg class="w-5 h-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
        </svg>
        Copied!
      {:else}
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
        </svg>
        Copy
      {/if}
    </button>
    <button
      onclick={clear}
      class="flex items-center gap-2 px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg transition-colors"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
      </svg>
      Clear
    </button>
  </div>

  {@render footer?.()}
</div>
