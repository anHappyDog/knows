// alertStore.js
import { reactive, readonly } from 'vue';

const state = reactive({
  alerts: []
});

const methods = {
  addAlert(alert) {
    const id = Math.random().toString(36).substr(2, 9);
    state.alerts.push({ ...alert, id });

    // 如果设置了显示时间，则在指定时间后移除警告
    if (alert.timeout) {
      setTimeout(() => {
        methods.removeAlert(id);
      }, alert.timeout);
    }
  },
  removeAlert(id) {
    const index = state.alerts.findIndex(alert => alert.id === id);
    if (index !== -1) {
      state.alerts.splice(index, 1);
    }
  }
};

export default {
  state: readonly(state),
  methods
};