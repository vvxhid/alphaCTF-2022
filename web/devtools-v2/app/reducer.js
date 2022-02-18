import { actionTypes } from "./actions";
import { HYDRATE } from "next-redux-wrapper";

const initialState = {
  flag: null,
};

function reducer(state=initialState, action) {
  switch (action?.type) {
    case HYDRATE: {
      return { ...state, ...action?.payload };
    }
    case actionTypes?.GET_FLAG:
      const new_state = { ...state, flag: "alphaCTF{aw3s00000000me_D3vT000000000Ls}" }
      return new_state;
    default:
      return state;
  }
}

export default reducer;
