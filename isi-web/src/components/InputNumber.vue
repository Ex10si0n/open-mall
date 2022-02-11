<script lang="ts" setup>
import { computed, ref, defineProps } from "vue";
import axios from "axios";
import config from "../config";
import { useStore } from "vuex";
import InputNumber from "../components/InputNumber.vue";

const store = useStore();

const accId = computed(() => {
  return store.state.accId;
});

defineProps<{ value: number }>();

const updateValue = (v: number) => {
  console.log(v);
};
</script>

<template>
  <n-space vertical class="w-36">
    <n-input-number min="1" @update:value="updateValue" :value="value" size="small">
      <template #prefix>Qty</template>
    </n-input-number>
  </n-space>
</template>
