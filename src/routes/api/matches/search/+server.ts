import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const POST: RequestHandler = async ({ request }) => {
    const db = await connection()
    const { matches, player1, player2 } = await request.json()


    const parsed = matches.map((value: string) => value.split('-'))
    console.log({ parsed, player1, player2 });

    let results = []

    for (let index = 0; index < parsed.length; index++) {
        const [rows] = await db.execute(`SELECT * FROM match_result WHERE year=? AND tourney_name LIKE ? AND ((winner LIKE ? and loser LIKE ?) OR (winner LIKE ? AND loser LIKE ?))`, [
            parseInt(parsed[index][0].substr(0, 4)),
            parsed[index][2],
            player1,
            player2,
            player2,
            player1
        ])
        console.log(rows);
        results.push({ ...rows[0], match_id: parsed[index].join('-') })
    }


    // console.log(rows.filter(row => row['set'] === 'Total'));

    return new Response(JSON.stringify(results.sort((a, b) => a.match_id - b.match_id)))
}