import { makeAutoObservable } from "mobx";
import { createUser } from "../components/fetches";

class PageStore {
  name = null;
  telegram_id = null;
  phone = null;
  count_bonus = null;
  referal = null;
  cart = [];

  constructor() {
    makeAutoObservable(this);
  }
  updateCart = (newCart) => {
    this.cart = newCart;
  };
  
  firstCreateUser = async (values) => {
    const result = await createUser(values);
    this.count_bonus = result.count_bonus;
    this.name = result.name;
    this.phone = result.phone;
    this.referal = result.referal;
    this.telegram_id = result.telegram_id;
  };
  signIn = async (telegram_id, values) => {
    const response = await fetch(
      `https://stvol.garden:8888/signin/?telegram_id=${telegram_id}`,
      {
        method: "POST",
        headers: { accept: "application/json" },
      }
    );
    const result = await response.json();
    console.log(response);
    if (response.status == 404) {
      await this.firstCreateUser(values);
    } else if (response.status == 200) {
      this.count_bonus = result?.count_bonus;
      this.name = result?.name;
      this.phone = result?.phone;
      this.referal = result?.referal;
      this.telegram_id = result?.telegram_id;
    }
  };
}

export default PageStore;
