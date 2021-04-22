import * as Types from "./types";
import axios from "axios";

axios.defaults.baseURL = "http://api-finance-docs.mhealthkenya.co.ke/api/";

export const getProjects = (data) => {
  return {
    type: Types.GET_PROJECTS,
    payload: data,
  };
};

export const getProjectsFail = (error) => {
  return {
    type: Types.GET_PROJECTS_FAIL,
    payload: error,
  };
};

export const requestProjects = () => {
  return (dispatch) => {
    const url = "projects/";
    axios
      .get(url)
      .then((res) => {
        const { data } = res;
        dispatch(getProjects(data));
      })
      .catch((err) => {
        const { message } = err;
        dispatch(getProjectsFail(message));
      });
  };
};
