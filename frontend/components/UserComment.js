import React from "react";
import { useState, useEffect } from "react";
import styles from "@/styles/Form.module.scss";
import { parseCookies } from "@/helpers/index";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { API_URL } from "@/config/index";
import Image from "next/image";
import { FaHighlighter, FaUser } from "react-icons/fa";


export default function UserComment({ eventId }) {
  const [values, setValues] = useState({
    username: "",
    comment: "",
    eventId: eventId,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    const hasEmptyFields = Object.values(values).some(
      (element) => element === ""
    );
    if (hasEmptyFields) {
      toast.error("Please fill in all fields");
      return;
    }

    const res = await fetch(`${API_URL}/comment`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(values),
    });
    if (!res.ok) {
      if (res.status === 403 || res.status === 401) {
        toast.error("No token included");
        return;
      }
      toast.error("Something Went Wrong");
    }
    if(!hasEmptyFields){
    if (res.ok) {
      if (res.status===200) {
        toast.success("Added new comment");
        return;
      }
    }
  }
  setValues({ username: "", comment: "" });// reset na nista poslije spremanja u bazu

  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    console.log("name", name)
    setValues({ ...values, [name]: value});
    //, [comment]: value 
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className={styles.form}>
        <div>
          <div>
            <label htmlFor="name" className="crvena">
              <FaUser /> Username:
            </label>
            <input
              type="text"
              id="name"
              name="username"
              value={values.username}
              onChange={handleInputChange}
            />
          </div>

          <div>
            <label htmlFor="name" className="crvena">
              <FaHighlighter /> Comment:
            </label>
            <textarea
              placeholder="Write a comment"
              id="textarea"
              name="comment"
              value={values.comment}
              onChange={handleInputChange}
              rows={5}
              cols={110}
            />
          </div>
          <div className={styles.link}>
            <input type="submit" value="Add Comment" className="btn" />
          </div>
        </div>
      </form>
    </div>
  );
}

//export default UserComment
export async function getServerSideProps({ req }) {
  const { token } = parseCookies(req);
  return {
    props: {
      token,
    },
  };
}
