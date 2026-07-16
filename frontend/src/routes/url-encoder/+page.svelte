<script lang="ts">
  import EncoderDecoderTool from '$lib/components/EncoderDecoderTool.svelte';

  let encodeType = $state<'component' | 'full'>('component');

  function transform(input: string, mode: 'encode' | 'decode'): string {
    if (mode === 'encode') {
      return encodeType === 'component'
        ? encodeURIComponent(input)
        : encodeURI(input);
    }
    return encodeType === 'component'
      ? decodeURIComponent(input)
      : decodeURI(input);
  }
</script>

<EncoderDecoderTool
  title="URL Encoder/Decoder"
  description="Encode or decode URL components and full URLs."
  encodedLabel="URL Encoded"
  decodePlaceholder="Enter URL-encoded text to decode..."
  decodeError="Invalid URL-encoded string"
  {transform}
>
  {#snippet controls()}
    <div class="flex gap-2">
      <button
        onclick={() => encodeType = 'component'}
        class="px-4 py-2 rounded-lg transition-colors {encodeType === 'component' ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
      >
        Component
      </button>
      <button
        onclick={() => encodeType = 'full'}
        class="px-4 py-2 rounded-lg transition-colors {encodeType === 'full' ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
      >
        Full URL
      </button>
    </div>
  {/snippet}

  {#snippet info()}
    {#if encodeType === 'component'}
      <p class="text-gray-300"><strong>Component mode:</strong> Encodes all special characters including <code class="bg-gray-700 px-1 rounded">/ ? & = #</code></p>
      <p class="text-gray-400 mt-1">Use for query parameters or path segments.</p>
    {:else}
      <p class="text-gray-300"><strong>Full URL mode:</strong> Preserves URL structure characters like <code class="bg-gray-700 px-1 rounded">/ ? & = # :</code></p>
      <p class="text-gray-400 mt-1">Use for complete URLs.</p>
    {/if}
  {/snippet}
</EncoderDecoderTool>
