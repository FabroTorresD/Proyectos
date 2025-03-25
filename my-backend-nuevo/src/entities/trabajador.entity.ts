import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Trabajador{

    @PrimaryGeneratedColumn()
    id: number; 

    @Column()
    name : string;

    @Column()
    fechanacimiento : Date

    @Column()
    id_area :number; 

}



