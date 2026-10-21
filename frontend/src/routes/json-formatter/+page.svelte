<script lang="ts">
  import EncoderDecoderTool from '$lib/components/EncoderDecoderTool.svelte';

  const indentOptions = [2, 4, 'tab'] as const;

  let indent = $state<(typeof indentOptions)[number]>(2);

  function transform(input: string, mode: 'encode' | 'decode'): string {
    const parsed = JSON.parse(input);
    if (mode === 'decode') return JSON.stringify(parsed);
    return JSON.stringify(parsed, null, indent === 'tab' ? '\t' : indent);
  }
</script>

<EncoderDecoderTool
  title="JSON Formatter"
  description="Format, validate and minify JSON."
  encodedLabel="Formatted JSON"
  decodePlaceholder="Enter JSON to minify..."
  encodeError="Invalid JSON"
  decodeError="Invalid JSON"
  {transform}
>
  {#snippet controls(mode)}
    {#if mode === 'encode'}
      <div class="flex gap-2">
        {#each indentOptions as option}
          <button
            onclick={() => indent = option}
            class="px-4 py-2 rounded-lg transition-colors {indent === option ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-300 hover:bg-gray-600'}"
          >
            {option === 'tab' ? 'Tab' : `${option} spaces`}
          </button>
        {/each}
      </div>
    {/if}
  {/snippet}

  {#snippet info(mode)}
    {#if mode === 'encode'}
      <p class="text-gray-300"><strong>Format mode:</strong> Validates the input and re-indents it.</p>
      <p class="text-gray-400 mt-1">Object keys keep their original order; comments and trailing commas are not valid JSON and will be rejected.</p>
    {:else}
      <p class="text-gray-300"><strong>Minify mode:</strong> Strips every optional whitespace character.</p>
      <p class="text-gray-400 mt-1">Use Swap to send a minified result back as input.</p>
    {/if}
  {/snippet}
</EncoderDecoderTool>
