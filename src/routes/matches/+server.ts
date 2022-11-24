import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const GET: RequestHandler = async ({ url }) => {
    const db = await connection()
    const player1 = `%${url.searchParams.get('player1')}%`
    const player2 = `%${url.searchParams.get('player2')}%`

    console.log({ player1, player2 });

    const [rows] = await db.execute(`SELECT match_id FROM match_meta WHERE (UPPER(Player_1) LIKE ? AND UPPER(Player_2) LIKE ?) OR (UPPER(Player_2) LIKE ? AND UPPER(Player_1) LIKE ?)`, [player1, player2, player1, player2])
    console.log({ rows, count: rows.length });

    return new Response(JSON.stringify(rows.map(value => value.match_id)))
}