import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { ChakraProvider } from "@chakra-ui/react";
import { RootStoreContext } from "./store/store_context";
import RootStore from "./store/root_store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <RootStoreContext.Provider value={new RootStore()}>
    <ChakraProvider>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </ChakraProvider>
  </RootStoreContext.Provider>
);
