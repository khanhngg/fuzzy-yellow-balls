import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const POST: RequestHandler = async ({ request }) => {
    const db = await connection()
    const { match, player1 }: { match: string, player1: boolean } = await request.json()

    console.log({ match, player1 });

    const [outcome,] = await db.execute(`SELECT * FROM shotdir_outcome WHERE match_id=? AND player=?`, [match, player1 ? 1 : 2])

    // console.log(rows.filter(row => row['set'] === 'Total'));

    return new Response(JSON.stringify({  outcome }))
}