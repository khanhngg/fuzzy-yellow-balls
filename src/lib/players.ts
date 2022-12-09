export default async (input: string) => {
    console.log(input);

    const res = await fetch(`/api/players/search?input=${input}`)
    const data = await res.json()
    console.log(data);

    return data
}