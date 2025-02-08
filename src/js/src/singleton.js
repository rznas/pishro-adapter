// singletonModel.js
class SingletonModel {
  constructor() {
    if (SingletonModel.instance) {
      return SingletonModel.instance;
    }
    this.data = null; // Placeholder for the initialization data
    SingletonModel.instance = this;
  }

  init(data) {
    if (this.data) {
      throw new Error("SingletonModel has already been initialized.");
    }
    this.data = data;
  }

  getData() {
    return this.data;
  }
}

module.exports = new SingletonModel();
