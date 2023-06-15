<template>
  <div>
    <nav>
      <ul>
        <li @click="currentTab = 'cpu'">CPU Info</li>
        <li @click="currentTab = 'memory'">Memory Info</li>
        <li @click="currentTab = 'battery'">Battery Info</li>
        <li @click="currentTab = 'general'">General System Info</li>
        <li @click="currentTab = 'disk'">Disk Info</li>
      </ul>
    </nav>

    <div v-show="currentTab === 'cpu'">
      <h2>CPU Info</h2>
      <p>CPU Usage: {{ cpuInfo?.['CPU Usage'] }}%</p>
      <p>Freqency: {{cpuInfo?.['Freqency Mhz'] }} Mhz</p>
      <p>CPU Cores: {{ cpuInfo?.['CPU cores'] }}</p>
      <p>Physical Cores: {{ cpuInfo?.['Physical cores'] }}</p>
      <p>Main CPU Core: CPU_{{ cpuInfo?.['Main CPU Core'] }}</p>
    </div>

    <div v-show="currentTab === 'memory'">
      <h2>Memory Info</h2>
      <p>Total Memory: {{ memoryInfo?.['Total Memory'] }}</p>
      <p>Available Memory: {{ memoryInfo?.['Available Memory'] }}</p>
      <p> Used Memory: {{ memoryInfo?.['Used Memory'] }}</p>
      <p> Available Memory percent: {{ memoryInfo?.['Available Memory per %'] }}%</p>
      <p> Used Memory percent: {{ memoryInfo?.['Used Memory per % '] }}%</p>
    </div>

    <div v-show="currentTab === 'battery'">
      <h2>Battery Info</h2>
      <p>Battery Percentage: {{ batteryInfo?.['Battery Percentage '] }}%</p>
      <p>Battery Charging: {{ batteryInfo?.['Plugged in '] ? 'Yes' : 'No' }}</p>
      <p>Charging Time: {{ batteryInfo?.['Charging time'] }}</p>
      <p>Remaining Time: {{ batteryInfo?.['Remaining time '] }}</p>
      <p>Status: {{ batteryInfo?.['Status'] }}</p>
    </div>

    <div v-show="currentTab === 'general'">
      <h2>General System Info</h2>
      <p>System Platform: {{ generalInfo?.['System Platform'] }}</p>
      <p>System Architecture: {{ generalInfo?.['System Architecture'] }}</p>
      <p>Operating System: {{ generalInfo?.['Operating System'] }}</p>
      <p>Operating System Release: {{ generalInfo?.['Operating System Release'] }}</p>
      <p>System Date: {{ generalInfo?.['System Date'] }}</p>
      <p>System Time: {{ generalInfo?.['System Time'] }}</p>
      <p>Processor: {{ generalInfo?.['Processor'] }}</p>
      <p>Distribution Name: {{ generalInfo?.['Distribution Name'] }}</p>
      <p>Distribution Version: {{ generalInfo?.['Distribution Version'] }}</p>
      <p>Distribution ID: {{ generalInfo?.['Distribution ID'] }}</p>
    </div>

    <div v-show="currentTab === 'disk'">
      <h2>Disk Info</h2>
      <div v-for="(partition, index) in diskInfo.partitionInfo" :key="index">
        <p>Device: {{ partition.Device }}</p>
        <p>Mountpoint: {{ partition.Mountpoint }}</p>
        <p>File System Type: {{ partition['File System Type'] }}</p>
        <p>Mount Options: {{ partition['Mount Options'] }}</p>
      </div>
      <p>Percentage Used: {{ diskInfo.diskUsageInfo?.['Percentage Used'] }}%</p>
      <p>Free Space: {{ diskInfo.diskUsageInfo?.['Free Space'] }}</p>
      <p>Used Space: {{ diskInfo.diskUsageInfo?.['Used Space'] }}</p>
      <p>Total Space: {{ diskInfo.diskUsageInfo?.['Total Space'] }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      currentTab: 'cpu',
      cpuInfo: null,
      memoryInfo: null,
      batteryInfo: null,
      generalInfo: null,
      diskInfo: {
        partitionInfo: [],
        diskUsageInfo: null
      }
    };
  },
  mounted() {
    this.getCpuInfo();
    this.getMemoryInfo();
    this.getBatteryInfo();
    this.getGeneralInfo();
    this.getDiskInfo();
  },
  methods: {
    getCpuInfo() {
      axios.get('http://localhost:5000/cpu')
        .then(response => {
          this.cpuInfo = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getMemoryInfo() {
      axios.get('http://localhost:5000/memory')
        .then(response => {
          this.memoryInfo = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getBatteryInfo() {
      axios.get('http://localhost:5000/battery')
        .then(response => {
          this.batteryInfo = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getGeneralInfo() {
      axios.get('http://localhost:5000/general')
        .then(response => {
          this.generalInfo = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getDiskInfo() {
      axios.get('http://localhost:5000/disk')
        .then(response => {
          this.diskInfo.partitionInfo = response.data[0];
          this.diskInfo.diskUsageInfo = response.data[1];
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
