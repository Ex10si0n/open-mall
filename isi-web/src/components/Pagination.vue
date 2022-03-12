<script setup lang="ts">
import { defineComponent, ref } from 'vue'

const props = defineProps<{ page: string; count: number }>();

</script>

<template>
  <n-pagination v-model:page="props.page" :page-count="props.count" :page-slot="3" show-quick-jumper />
</template>

<script lang="ts">

</script>