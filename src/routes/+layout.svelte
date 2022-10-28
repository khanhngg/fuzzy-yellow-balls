<script lang="ts">
  import Header from '$lib/header/Header.svelte';
  import '../app.postcss';
</script>

<Header />

<main>
  <slot />
</main>

<footer class="mt-auto">
  <p><a href="https://github.com/khanhngg/fuzzy-yellow-balls" target="_blank">GitHub</a></p>
  <p>&#xa9; 2022. All rights reserved.</p>
</footer>

<style>
  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
    max-width: 1024px;
    margin: 0 auto;
    box-sizing: border-box;
  }

  footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }

  footer a {
    font-weight: bold;
  }

  @media (min-width: 480px) {
    footer {
      padding: 40px 0;
    }
  }
</style>
