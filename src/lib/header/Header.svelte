<script lang="ts">
  import { DarkMode } from 'flowbite-svelte';
  import { page } from '$app/stores';
  import logo from './fuzzy-yellow-bird.png';
</script>

<header>
  <div class="corner pl-3 pt-1">
    <a href="/">
      <img src={logo} alt="Fuzzy Yellow Bird Logo" />
    </a>
  </div>

  <nav data-sveltekit-prefetch>
    <svg viewBox="0 0 2 3" aria-hidden="true">
      <path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
    </svg>
    <ul>
      <li class:active={$page.url.pathname === '/'}>
        <a class="text-gray-300" href="/">Home</a>
      </li>
      <li class:active={$page.url.pathname === '/players'}>
        <a class="text-gray-300" href="/players">Players</a>
      </li>
      <li class:active={$page.url.pathname === '/matches'}>
        <a class="text-gray-300" href="/matches">Matches</a>
      </li>
      <li class:active={$page.url.pathname === '/surfaces'}>
        <a class="text-gray-300" href="/surfaces">Surfaces</a>
      </li>
      <li class:active={$page.url.pathname === '/rankings'}>
        <a class="text-gray-300" href="/rankings">Rankings</a>
      </li>
    </ul>
    <svg viewBox="0 0 2 3" aria-hidden="true">
      <path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
    </svg>
  </nav>

  <div class="corner pt-1">
    <DarkMode btnClass="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 fixed left-0 top-8 z-50 header-button" />
  </div>
</header>

<style>
  header {
    display: flex;
    justify-content: space-between;
  }

  .corner {
    width: 3em;
    height: 3em;
  }

  .corner a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
  }

  .corner img {
    width: 2em;
    height: 2em;
    object-fit: contain;
  }

  .corner :global(.header-button) {
    position: unset;
  }

  nav {
    display: flex;
    justify-content: center;
    --background: rgba(22, 25, 32, 0.9);
  }

  svg {
    width: 2em;
    height: 3em;
    display: block;
  }

  path {
    fill: var(--background);
  }

  ul {
    position: relative;
    padding: 0;
    margin: 0;
    height: 3em;
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    background: var(--background);
    background-size: contain;
  }

  li {
    position: relative;
    height: 100%;
  }

  li.active::before {
    --size: 6px;
    content: '';
    width: 0;
    height: 0;
    position: absolute;
    top: 0;
    left: calc(50% - var(--size));
    border: var(--size) solid transparent;
    border-top: var(--size) solid var(--accent-color);
  }

  nav a {
    display: flex;
    height: 100%;
    align-items: center;
    padding: 0 1em;
    font-weight: 700;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    text-decoration: none;
    transition: color 0.2s linear;
  }

  a:hover {
    color: var(--accent-color);
  }
</style>
