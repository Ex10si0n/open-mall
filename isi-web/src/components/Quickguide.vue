<script setup lang="ts">

defineProps<{ msg: string }>();

// const count = ref(0)
</script>

<template>
  <div class="my-2 leading-8 max-w-screen-sm text-left mx-auto">
    <h1 class="text-4xl text-gray-600 font-bold py-5">{{ msg }}</h1>
    You can remove or replace necessary properties in
    <span class="whitespace-pre font-mono bg-slate-100 p-0.5 rounded shadow-md"
    >src/views/Home.vue</span
    >
    to remove or change
    <a class="underline decoration-pink-500 decoration-2">router links</a>. Plus, you can
    create or edit this Vue Component at
    <span class="whitespace-pre font-mono bg-slate-100 p-0.5 rounded shadow-md"
    >src/components/Quickguide.vue</span
    >
    to create new one or customize this
    <a class="underline decoration-pink-500 decoration-2">component</a>.
  </div>
</template>

<style scoped></style>
