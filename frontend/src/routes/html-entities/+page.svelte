<script lang="ts">
  let input = $state('');
  let output = $state('');
  let mode = $state<'encode' | 'decode'>('encode');
  let encodeType = $state<'named' | 'numeric' | 'hex'>('named');
  let error = $state('');
  let copied = $state(false);

  const namedEntities: Record<string, string> = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
    ' ': '&nbsp;',
    '©': '&copy;',
    '®': '&reg;',
    '™': '&trade;',
    '€': '&euro;',
    '£': '&pound;',
    '¥': '&yen;',
    '¢': '&cent;',
    '§': '&sect;',
    '°': '&deg;',
    '±': '&plusmn;',
    '×': '&times;',
    '÷': '&divide;',
    '←': '&larr;',
    '→': '&rarr;',
    '↑': '&uarr;',
    '↓': '&darr;',
    '♠': '&spades;',
    '♣': '&clubs;',
    '♥': '&hearts;',
    '♦': '&diams;',
  };

  const reverseNamedEntities: Record<string, string> = Object.fromEntries(
    Object.entries(namedEntities).map(([k, v]) => [v, k])
  );

  function encodeHtml(text: string, type: 'named' | 'numeric' | 'hex'): string {
    let result = '';
    for (const char of text) {
      if (type === 'named' && namedEntities[char]) {
        result += namedEntities[char];
      } else if (char.charCodeAt(0) > 127 || '<>&"\''.includes(char)) {
        if (type === 'hex') {
          result += `&#x${char.charCodeAt(0).toString(16)};`;
        } else {
          result += `&#${char.charCodeAt(0)};`;
        }
      } else {
        result += char;
      }
    }
    return result;
  }

  function decodeHtml(text: string): string {
    // First decode named entities
    let result = text;
    for (const [entity, char] of Object.entries(reverseNamedEntities)) {
      result = result.replaceAll(entity, char);
    }

    // Then decode numeric entities (decimal)
    result = result.replace(/&#(\d+);/g, (_, code) => {
      return String.fromCharCode(parseInt(code, 10));
    });

    // Then decode hex entities
    result = result.replace(/&#x([0-9a-fA-F]+);/g, (_, code) => {
      return String.fromCharCode(parseInt(code, 16));
    });

    return result;
  }

  function process() {
    error = '';
    if (!input) {
      output = '';
      return;
    }

    try {
      if (mode === 'encode') {
        output = encodeHtml(input, encodeType);
      } else {
        output = decodeHtml(input);
      }
    } catch (e) {
      error = 'Processing error';
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
    input;
    mode;
    encodeType;
    process();
  });
</script>

<div class="max-w-4xl mx-auto">
  <h1 class="text-3xl font-bold mb-2">HTML Entity Encoder</h1>
  <p class="text-gray-400 mb-8">Convert special characters to HTML entities and vice versa.</p>

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
    {#if mode === 'encode'}
      <div class="flex gap-2">
        <button
          onclick={() => encodeType = 'named'}
          class="px-4 py-2 rounded-lg transition-colors {encodeType === 'named' ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
        >
          Named
        </button>
        <button
          onclick={() => encodeType = 'numeric'}
          class="px-4 py-2 rounded-lg transition-colors {encodeType === 'numeric' ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
        >
          Numeric
        </button>
        <button
          onclick={() => encodeType = 'hex'}
          class="px-4 py-2 rounded-lg transition-colors {encodeType === 'hex' ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
        >
          Hex
        </button>
      </div>
    {/if}
  </div>

  <!-- Info box -->
  <div class="bg-gray-800 border border-gray-700 rounded-lg p-4 mb-6 text-sm">
    {#if mode === 'encode'}
      {#if encodeType === 'named'}
        <p class="text-gray-300"><strong>Named entities:</strong> <code class="bg-gray-700 px-1 rounded">&amp;amp;</code> <code class="bg-gray-700 px-1 rounded">&amp;lt;</code> <code class="bg-gray-700 px-1 rounded">&amp;copy;</code></p>
      {:else if encodeType === 'numeric'}
        <p class="text-gray-300"><strong>Numeric entities:</strong> <code class="bg-gray-700 px-1 rounded">&amp;#38;</code> <code class="bg-gray-700 px-1 rounded">&amp;#60;</code> <code class="bg-gray-700 px-1 rounded">&amp;#169;</code></p>
      {:else}
        <p class="text-gray-300"><strong>Hex entities:</strong> <code class="bg-gray-700 px-1 rounded">&amp;#x26;</code> <code class="bg-gray-700 px-1 rounded">&amp;#x3c;</code> <code class="bg-gray-700 px-1 rounded">&amp;#xa9;</code></p>
      {/if}
    {:else}
      <p class="text-gray-300">Decodes all entity formats: named, numeric, and hex.</p>
    {/if}
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
    <!-- Input -->
    <div>
      <div class="flex justify-between items-center mb-2">
        <label for="input" class="text-sm text-gray-400">
          {mode === 'encode' ? 'Text' : 'HTML Entities'}
        </label>
        <span class="text-xs text-gray-500">{input.length} chars</span>
      </div>
      <textarea
        id="input"
        bind:value={input}
        placeholder={mode === 'encode' ? 'Enter text to encode...' : 'Enter HTML entities to decode...'}
        class="w-full h-64 p-4 bg-gray-800 border border-gray-700 rounded-lg font-mono text-sm resize-none focus:outline-none focus:border-blue-500"
      ></textarea>
    </div>

    <!-- Output -->
    <div>
      <div class="flex justify-between items-center mb-2">
        <label for="output" class="text-sm text-gray-400">
          {mode === 'encode' ? 'HTML Entities' : 'Text'}
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

  <!-- Common Entities Reference -->
  <div class="mt-8">
    <h2 class="text-lg font-semibold mb-4">Common HTML Entities</h2>
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
      {#each Object.entries(namedEntities).slice(0, 18) as [char, entity]}
        <div class="bg-gray-800 border border-gray-700 rounded-lg p-3 text-center">
          <div class="text-2xl mb-1">{char}</div>
          <code class="text-xs text-gray-400">{entity}</code>
        </div>
      {/each}
    </div>
  </div>
</div>
