<template>
  <div id="app">
    <button>Select a Winner</button>
    <p>
      {{names}}
    </p>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
      return {
          names: null,
          winner: null,
      }
  },
  mounted: function() {
    this.FetchData();
  },
  methods: {
      FetchData: function() {
          var app = this;
          axios.get("/api/product/").then(response => {
              app.names = response.data;
          });
      },
      // SelectWinner: function() {
      //   var winner = this.names[Math.floor(Math.random()*this.names.length)];
      //   this.winner = winner;
      // },
  }
}
</script>
<style>
</style>
