<script lang="ts">
  import EncoderDecoderTool from '$lib/components/EncoderDecoderTool.svelte';

  // Claims whose value is a NumericDate (seconds since epoch) per RFC 7519.
  const dateClaims = ['exp', 'iat', 'nbf', 'auth_time', 'updated_at'];

  function decodeSegment(segment: string): unknown {
    // base64url -> base64, then percent-decode the bytes so UTF-8 survives.
    const base64 = segment.replace(/-/g, '+').replace(/_/g, '/');
    const binary = atob(base64.padEnd(Math.ceil(base64.length / 4) * 4, '='));
    const json = decodeURIComponent(
      Array.from(binary, (c) => `%${c.charCodeAt(0).toString(16).padStart(2, '0')}`).join('')
    );
    return JSON.parse(json);
  }

  function readableDates(payload: unknown): Record<string, string> {
    if (typeof payload !== 'object' || payload === null) return {};

    const now = Date.now();
    const readable: Record<string, string> = {};

    for (const [claim, value] of Object.entries(payload)) {
      if (!dateClaims.includes(claim) || typeof value !== 'number') continue;
      const date = new Date(value * 1000);
      if (Number.isNaN(date.getTime())) continue;

      let note = '';
      if (claim === 'exp') note = date.getTime() < now ? ' (expired)' : ' (valid)';
      if (claim === 'nbf' && date.getTime() > now) note = ' (not valid yet)';
      readable[claim] = date.toISOString() + note;
    }

    return readable;
  }

  function transform(input: string): string {
    const parts = input.trim().split('.');
    if (parts.length !== 3) {
      throw new Error('A JWT has three dot-separated segments');
    }

    const [header, payload, signature] = parts;
    const claims = decodeSegment(payload);

    return JSON.stringify(
      {
        header: decodeSegment(header),
        payload: claims,
        readable: readableDates(claims),
        signature
      },
      null,
      2
    );
  }
</script>

<EncoderDecoderTool
  title="JWT Decoder"
  description="Decode and inspect JWT header and payload."
  encodedLabel="JWT"
  decodePlaceholder="Paste a JWT (eyJhbGciOi...)"
  decodeError="Not a valid JWT: expected three dot-separated base64url segments holding JSON"
  modes={['decode']}
  {transform}
>
  {#snippet info()}
    <p class="text-gray-300"><strong>The signature is not verified.</strong> Decoding only reads the token; it proves nothing about who issued it.</p>
    <p class="text-gray-400 mt-1">A JWT is signed, not encrypted — treat anything inside it as public. Never paste a production token you still rely on.</p>
  {/snippet}

  {#snippet footer()}
    <div class="mt-8 bg-gray-800 border border-gray-700 rounded-lg p-4 text-sm">
      <h2 class="font-semibold mb-2">Date claims</h2>
      <p class="text-gray-400">
        <code class="bg-gray-700 px-1 rounded">exp</code>,
        <code class="bg-gray-700 px-1 rounded">iat</code>,
        <code class="bg-gray-700 px-1 rounded">nbf</code>,
        <code class="bg-gray-700 px-1 rounded">auth_time</code> and
        <code class="bg-gray-700 px-1 rounded">updated_at</code>
        hold seconds since the Unix epoch. They are repeated as ISO dates under
        <code class="bg-gray-700 px-1 rounded">readable</code>, compared against your local clock.
      </p>
    </div>
  {/snippet}
</EncoderDecoderTool>
