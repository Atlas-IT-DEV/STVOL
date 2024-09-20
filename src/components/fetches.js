const baseUrl = "https://stvol.garden:8888";

export const getAllUsers = async () => {
  const response = await fetch(baseUrl + "/users/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const GetAllAdresses = async () => {
  const response = await fetch(baseUrl + "/adresses/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllOrders = async () => {
  const response = await fetch(baseUrl + "/orders/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllBouquets = async () => {
  const response = await fetch(baseUrl + "/bouquets/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllBouquetsFull = async () => {
  const response = await fetch(baseUrl + "/bouquets/full", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllCompanys = async () => {
  const response = await fetch(baseUrl + "/companys/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllRefcodes = async () => {
  const response = await fetch(baseUrl + "/refcodes/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAllImages = async () => {
  const response = await fetch(baseUrl + "/images/", {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getUserById = async (id) => {
  const response = await fetch(baseUrl + `/users/user_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getUserByTelegramId = async (id) => {
  const response = await fetch(baseUrl + `/users/telegram_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAdressById = async (id) => {
  const response = await fetch(baseUrl + `/adresses/adress_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getAdressByUserId = async (id) => {
  const response = await fetch(baseUrl + `/adresses/user_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getOrderById = async (id) => {
  const response = await fetch(baseUrl + `/orders/order_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getOrderByUserId = async (id) => {
  const response = await fetch(baseUrl + `/orders/user_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getHistoryOrder = async (id) => {
  const response = await fetch(baseUrl + `/orders/history/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getBouquetByUserId = async (id) => {
  const response = await fetch(baseUrl + `/bouquets/bouquet_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getBouquetByUserIdFull = async (id) => {
  const response = await fetch(baseUrl + `/bouquets/bouquet_id/full/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getBouquetByName = async (id) => {
  const response = await fetch(baseUrl + `/bouquets/bouquet_name/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getCompanyById = async (id) => {
  const response = await fetch(baseUrl + `/companys/company_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getRefcodeById = async (id) => {
  const response = await fetch(baseUrl + `/refcodes/refcode_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getRefcodeByUserId = async (id) => {
  const response = await fetch(baseUrl + `/refcodes/user_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getUserByRefcode = async (id) => {
  const response = await fetch(baseUrl + `/refcodes/refcode/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const getImageById = async (id) => {
  const response = await fetch(baseUrl + `/images/image_id/${id}`, {
    method: "GET",
    headers: {
      accept: "application/json",
    },
  });
  const result = await response.json();
  return result;
};

export const createUser = async (values) => {
  const response = await fetch(baseUrl + "/users/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify(values),
  });
  const result = await response.json();
  return result;
};

export const createAdress = async () => {
  const response = await fetch(baseUrl + "/adresses/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      adress: "",
      user_id: 0,
    }),
  });
  const result = await response.json();
  return result;
};

export const createOrder = async () => {
  const response = await fetch(baseUrl + "/orders/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      user_id: 0,
      date: "",
      total_price: 0,
    }),
  });
  const result = await response.json();
  return result;
};

export const createBouquet = async () => {
  const response = await fetch(baseUrl + "/bouquets/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      name: "",
      price: 0,
      image_id: 0,
    }),
  });
  const result = await response.json();
  return result;
};

export const createCompany = async () => {
  const response = await fetch(baseUrl + "/companys/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      name: "",
      description: "",
    }),
  });
  const result = await response.json();
  return result;
};

export const createRefcode = async () => {
  const response = await fetch(baseUrl + "/refcodes/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      user_id: 0,
      code: "",
    }),
  });
  const result = await response.json();
  return result;
};

export const createImage = async () => {
  const response = await fetch(baseUrl + "/images/", {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      id: 0,
      url: "",
    }),
  });
  const result = await response.json();
  return result;
};
