<template>
  <div id="app">
    <VideoContainer/>
  </div>
</template>

<script>
import VideoContainer from './components/VideoContainer.vue'

export default {
  name: 'App',
  components: {
    VideoContainer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
