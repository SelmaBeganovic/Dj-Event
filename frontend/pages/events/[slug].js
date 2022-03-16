import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Link from "next/link";
import Image from "next/image";
import Layout from "@/components/Layout";
import { API_URL } from "@/config/index";
import styles from "@/styles/Event.module.scss";
import UserComment from "components/UserComment";
import CommentItem from "@/components/CommentItem";
import Rating from "@/components/Rating"
import user from "pages/api/user";
import { parseCookies } from "@/helpers/index";


export default function EventPage({ evt, comments,token ,ratings}) {
  console.log("comments", comments);
  console.log("evt", evt);
  console.log("user", user);
  console.log("ispis ratinga sa backenda",ratings)

  return (
    <Layout>
      <div className={styles.event}>
        <span>
          {new Date(evt.date).toLocaleDateString("en-US")} at {evt.time}
        </span>
        <h1>{evt.name}</h1>
        <ToastContainer />
        {evt.image && (
          <div className={styles.image}>
            <Image src={evt.image} width={960} height={600} />
          </div>
        )}

        <h3>Performers:</h3>
        <p>{evt.performers}</p>
        <h3>Description:</h3>
        <p>{evt.description}</p>
        <h3>Venue: {evt.venue}</h3>
        <p>{evt.address}</p>

       
       <h3>Users Ratings</h3>
       <Rating key={evt.id} eventId={evt.id} token={token}/>
      
       <p className="p_rating">
          Prosjecna vrijednost ratinga je:  {ratings.toFixed(2)} 
       </p>
          
        
        <h3 className="crvena"> User Comments:</h3> 
        {comments.map((comment) => (
          <CommentItem key={comment.id}
            username={comment.username}
            comment={comment.comment}
            created_at={comment.created_at}
          />
        ))
        }

        <UserComment eventId={evt.id}/>

        <Link href="/events">
          <a className={styles.back}>{"<"} Go Back</a>
        </Link>
      </div>
    </Layout>
  );
}

export async function getServerSideProps({ query: { slug }, req }) {
  const res = await fetch(`${API_URL}/events?slug=${slug}`);
  const events = await res.json();

  const comment = await fetch(`${API_URL}/comment/${events[0].id}`);
  const comments = await comment.json();
  const { token } = parseCookies(req);

  const rating = await fetch(`${API_URL}/rating/${events[0].id}`);
  const ratings = await rating.json();

  return {
    props: {
      evt: events[0],
      comments: comments,
      token,
      ratings,
    },
  };
}
