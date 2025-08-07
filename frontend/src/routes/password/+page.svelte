<script>
  import { onMount } from 'svelte';

  let password = '';
  let length = 12;

  let includeLowercase   = true;
  let includeUppercase   = true;
  let includeNumbers     = true;
  let includeSpecial     = true;

  async function generatePassword() {
    try {
      const params = new URLSearchParams({
        length:   String(length),
        lower:    includeLowercase ? 'true' : 'false',
        upper:    includeUppercase ? 'true' : 'false',
        digits:   includeNumbers   ? 'true' : 'false',
        special:  includeSpecial   ? 'true' : 'false'
      });

      const res = await fetch(`/api/password/?${params.toString()}`);
      if (!res.ok) {
        throw new Error(`Error ${res.status}`);
      }
      const { password: pwd } = await res.json();
      password = pwd;
    } catch (err) {
      console.error(err);
      password = 'Something went wrong';
    }
  }
  onMount(generatePassword);
</script>

<main class="p-4 space-y-4 max-w-md mx-auto">
  <h1 class="text-2xl font-bold">Générateur de mot de passe</h1>

  <div class="space-y-2">
    <div>
      <label for="lower">Minuscules</label>
      <input
        id="lower"
        type="checkbox"
        bind:checked={includeLowercase}
        on:change={generatePassword}
      />
    </div>
    <div>
      <label for="upper">Majuscules</label>
      <input
        id="upper"
        type="checkbox"
        bind:checked={includeUppercase}
        on:change={generatePassword}
      />
    </div>
    <div>
      <label for="digits">Chiffres</label>
      <input
        id="digits"
        type="checkbox"
        bind:checked={includeNumbers}
        on:change={generatePassword}
      />
    </div>
    <div>
      <label for="special">Caractères spéciaux</label>
      <input
        id="special"
        type="checkbox"
        bind:checked={includeSpecial}
        on:change={generatePassword}
      />
    </div>
  </div>
  <div class="flex gap-2">
    <input
      class="flex-1 p-2 border rounded"
      readonly
      bind:value={password}
      placeholder="Mot de passe généré"
    />
    <button
      aria-label="Generate password"
      class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      on:click={generatePassword}
    >
      Generate
    </button>
  </div>
  <div>
    <label
      for="password-length"
      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
    >Longueur : {length}</label>
    <input
      id="password-length"
      class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
      type="range"
      min="4"
      max="64"
      bind:value={length}
      on:input={generatePassword}
    />
  </div>
</main>
