import { useState } from "react";
import styles from "@/styles/Form.module.scss";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { API_URL } from "@/config/index";
import { FaStar } from "react-icons/fa";

export default function Rating({ eventId, token }) {
  const [rating, setRating] = useState(null);
  const [hover, setHover] = useState(null);

  const handleClick = async (e, ratingValue) => {
    setRating(ratingValue);
    e.preventDefault();

    console.log("parse", parseInt(ratingValue));
    console.log("unesena vrijednost ista kao ratingvalue ", e.target.value);
    console.log("token", token);

    const res = await fetch(`${API_URL}/rating`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ rating: ratingValue, eventId: eventId }),
    });
    console.log("res", res);

    if (!res.ok) {
      if (res.status === 403 || res.status === 401) {
        toast.error("Please log in!");
        return;
      }
      toast.error("Something Went Wrong");
    } else {
      if (res.status === 200) {
        toast.success("Added rating");
        return;
      }
    }
  };

  return (
    <div>
      <form className={styles.form}>
        <div className="rating">
          <div>
            <div className="zvijezda">
              {[...Array(5)].map((star, i) => {
                const ratingValue = i + 1;
                return (
                  <label>
                    <input
                      key={`ratio-${ratingValue}`}
                      type="radio"
                      name="rating"
                      value={ratingValue}
                      onClick={(e) => {
                        handleClick(e, ratingValue);
                      }}
                    />

                    <FaStar
                      key={`star-${ratingValue}`}
                      className="star"
                      color={
                        ratingValue <= (hover || rating) ? "red" : "#e4e5e9"
                      }
                      size={50}
                      onMouseEnter={() => setHover(ratingValue)}
                      onMouseLeave={() => setHover(null)}
                    />
                  </label>
                );
              })}
            </div>
            <div className="p_rating">
              <p> Vasa vrijednost ratinga je {rating}</p>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}
