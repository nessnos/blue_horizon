<template>
  <div class="flex h-screen">
    <SideBar class="border-none" />
    <div class="flex flex-grow justify-center">
      <Chat />
    </div>
  </div>
</template>

<script lang="ts" setup>
import Chat from "@/components/pages/ChatPage.vue"
import SideBar from "@/components/share/SideBar.vue"
</script>
