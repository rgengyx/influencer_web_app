<template>
  <div>
    <iframe id="video-container" v-bind:src="url"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">
    </iframe>
<!--    <div id="url">-->
<!--      {{ url }}-->
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: 'VideoContainer',
  data() {
    return {
      url: null
    }
  },
  mounted() {
    this.fetchUrls()
  },
  methods: {
    fetchUrls() {
      const api = 'http://localhost:9808'
      this.$http.get(api)
          .then((result) => {
            this.url = Object.values(result.data)[0]
          })
    }
  }

}
</script>

<style scoped>

#video-container {
  width: 48em;
  height: 27em;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  maxWidth: 100%;
  maxHeight: 100%;
  overflow: auto;
  backgroundSize: 100%;
  boxShadow: 20px 10px 20px #888888, -10px -10px 20px #888888;
}

</style>
