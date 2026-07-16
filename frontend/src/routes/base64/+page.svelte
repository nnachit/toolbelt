<script lang="ts">
  import EncoderDecoderTool from '$lib/components/EncoderDecoderTool.svelte';

  function transform(input: string, mode: 'encode' | 'decode'): string {
    return mode === 'encode'
      ? btoa(unescape(encodeURIComponent(input)))
      : decodeURIComponent(escape(atob(input)));
  }
</script>

<EncoderDecoderTool
  title="Base64 Encoder/Decoder"
  description="Encode text to Base64 or decode Base64 to text."
  encodedLabel="Base64"
  decodeError="Invalid Base64 string"
  {transform}
/>
