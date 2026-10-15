<script lang="ts">
  import EncoderDecoderTool from '$lib/components/EncoderDecoderTool.svelte';

  let encodeType = $state<'named' | 'numeric' | 'hex'>('named');

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
      const codePoint = char.codePointAt(0)!;
      if (type === 'named' && namedEntities[char]) {
        result += namedEntities[char];
      } else if (codePoint > 127 || '<>&"\''.includes(char)) {
        if (type === 'hex') {
          result += `&#x${codePoint.toString(16)};`;
        } else {
          result += `&#${codePoint};`;
        }
      } else {
        result += char;
      }
    }
    return result;
  }

  function decodeHtml(text: string): string {
    // Single pass so already-decoded output is never decoded a second time
    // (e.g. "&amp;lt;" must yield "&lt;", not "<")
    return text.replace(
      /&(?:#[xX]([0-9a-fA-F]+)|#(\d+)|([a-zA-Z][a-zA-Z0-9]*));/g,
      (match, hex, decimal, name) => {
        if (hex) return String.fromCodePoint(parseInt(hex, 16));
        if (decimal) return String.fromCodePoint(parseInt(decimal, 10));
        return reverseNamedEntities[`&${name};`] ?? match;
      }
    );
  }

  function transform(input: string, mode: 'encode' | 'decode'): string {
    return mode === 'encode' ? encodeHtml(input, encodeType) : decodeHtml(input);
  }
</script>

<EncoderDecoderTool
  title="HTML Entity Encoder"
  description="Convert special characters to HTML entities and vice versa."
  encodedLabel="HTML Entities"
  decodePlaceholder="Enter HTML entities to decode..."
  {transform}
>
  {#snippet controls(mode)}
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
  {/snippet}

  {#snippet info(mode)}
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
  {/snippet}

  {#snippet footer()}
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
  {/snippet}
</EncoderDecoderTool>
