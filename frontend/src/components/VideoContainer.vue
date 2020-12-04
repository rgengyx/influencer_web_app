<template>
  <div id="video-container">
    <iframe id="video" v-bind:src="url"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">
    </iframe>
    <div id="thumbnail" v-on:click="thumbnailClick(); showThumbnail = true" v-if="!showThumbnail">
      <img src="../assets/image/thumbnail/food.jpg" />
      <img id="playbutton" src="../assets/misc/playbutton.svg" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoContainer',
  data() {
    return {
      url: null,
      showThumbnail: false
    }
  },

  // mounted(){
  //   this.fetchUrls()
  // },

  methods: {
    fetchUrls() {
      const api = 'http://localhost:9808'
      this.$http.get(api)
          .then((result) => {
            this.url = Object.values(result.data)[0] + "?autoplay=1&mute=1"
          })
    },
    thumbnailClick(){
      this.fetchUrls()
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
  overflow: hidden;
}

#thumbnail {
  height: 100%;
  width: 100%;
  right: 0;
  top: 0;
  position: absolute;
}

#thumbnail img{
  width:100%;
  right: 0;
  top: 0;
  position: absolute;
}

#thumbnail img#playbutton {
  height: 100%;
  opacity: 0.8;
}

#video {
  height: 100%;
  width: 100%;
  right: 0;
  top: 0;
  position: absolute;
}

</style>
