<template>
  <div>
    <button @click="getCpuInfo">Get CPU Info</button>
    <button @click="getMemoryInfo">Get Memory Info</button>
    <button @click="getBatteryInfo">Get Battery Info</button>
    <button @click="getGeneralInfo">Get General System Info</button>
    <button @click="getDiskInfo">Get Disk Info</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    getCpuInfo() {
      axios.get('http://localhost:5000/cpu')
        .then(response => {
          console.log(response.data); // Handle the CPU info response
        })
        .catch(error => {
          console.error(error);
        });
    },
    getMemoryInfo() {
      axios.get('http://localhost:5000/memory')
        .then(response => {
          console.log(response.data); // Handle the memory info response
        })
        .catch(error => {
          console.error(error);
        });
    },
    getBatteryInfo() {
      axios.get('http://localhost:5000/battery')
        .then(response => {
          console.log(response.data); // Handle the battery info response
        })
        .catch(error => {
          console.error(error);
        });
    },
    getGeneralInfo() {
      axios.get('http://localhost:5000/general')
        .then(response => {
          console.log(response.data); // Handle the general system info response
        })
        .catch(error => {
          console.error(error);
        });
    },
    getDiskInfo() {
      axios.get('http://localhost:5000/disk')
        .then(response => {
          console.log(response.data); // Handle the disk info response
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
