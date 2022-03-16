import styles from "@/styles/EventItem.module.scss";


export default function CommentItem({  username, comment , created_at }) {
  return (
    <div className={styles.event}>

      <div className={styles.info}>
       {username}
      </div>

      <div className={styles.info}>
       {comment}
      </div>

      <div className={styles.info}>
       {created_at}
      </div>

    </div>
  );
}

