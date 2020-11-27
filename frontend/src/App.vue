<template>
  <div id="app" v-on:mousemove="hover" v-on:mousedown="click">
    <VideoContainer/>
  </div>
</template>

<script>
import VideoContainer from './components/VideoContainer.vue'

export default {
  name: 'App',
  components: {
    VideoContainer
  },
  methods: {
    hover(event) {
      // screenX/Y gives the coordinates relative to the screen in device pixels.
      var screenX = event.screenX;
      var screenY = event.screenY;

      console.log("hover x", screenX);
      console.log("hover y", screenY);

      const api = 'http://localhost:9808/mouseEvent'

      this.$http.post(api, {
        timestamp: Date.now(),
        screenX: screenX,
        screenY: screenY,
        type: "hover"
      })
    },

    click(event) {
      // screenX/Y gives the coordinates relative to the screen in device pixels.
      var screenX = event.screenX;
      var screenY = event.screenY;

      console.log("click x", screenX);
      console.log("click y", screenY);

      const api = 'http://localhost:9808/mouseEvent'

      this.$http.post(api, {
        timestamp: Date.now(),
        screenX: screenX,
        screenY: screenY,
        type: "click"
      })
    }

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
  background-color: #888888;
  height: 100vh;
}
</style>
