import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getFlag } from "../actions";

const Index = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const date_now = new Date();
    if (date_now.getTime() === new Date(0xfffffffffffff).getTime()) {
      // free flag
      dispatch(getFlag());
    }
  }, [dispatch]);

  return (
    <div>
      <h1>Another next.js/redux app</h1>
    </div>
  );
};

export default Index;
